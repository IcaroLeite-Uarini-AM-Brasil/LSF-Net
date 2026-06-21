"""
LSF-Net Backend - Localizador de Seres Físicos em Rede
Aplicação Flask para gerenciamento de localização de dispositivos
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import json
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Inicializar Flask
app = Flask(__name__)
CORS(app)

# Configurações
app.config['JSON_SORT_KEYS'] = False
app.config['DEBUG'] = os.getenv('FLASK_ENV') == 'development'

# Dados em memória (em produção, use um banco de dados)
devices = {}
locations = {}

# ==================== HEALTH CHECK ====================

@app.route('/api/health', methods=['GET'])
def health_check():
    """Verificar status da aplicação"""
    return jsonify({
        'status': 'healthy',
        'message': 'LSF-Net Backend is running',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    }), 200

# ==================== DEVICES ====================

@app.route('/api/devices', methods=['GET'])
def get_devices():
    """Listar todos os dispositivos"""
    return jsonify({
        'success': True,
        'count': len(devices),
        'data': list(devices.values())
    }), 200

@app.route('/api/devices', methods=['POST'])
def create_device():
    """Registrar novo dispositivo"""
    try:
        data = request.get_json()
        
        # Validar dados obrigatórios
        if not data or 'name' not in data or 'mac_address' not in data:
            return jsonify({
                'success': False,
                'error': 'name e mac_address são obrigatórios'
            }), 400
        
        device_id = data.get('mac_address')
        
        # Evitar duplicatas
        if device_id in devices:
            return jsonify({
                'success': False,
                'error': 'Dispositivo já registrado'
            }), 409
        
        device = {
            'id': device_id,
            'name': data.get('name'),
            'mac_address': device_id,
            'type': data.get('type', 'unknown'),
            'status': 'online',
            'created_at': datetime.now().isoformat(),
            'last_seen': datetime.now().isoformat()
        }
        
        devices[device_id] = device
        
        return jsonify({
            'success': True,
            'message': 'Dispositivo registrado com sucesso',
            'data': device
        }), 201
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/devices/<device_id>', methods=['GET'])
def get_device(device_id):
    """Obter detalhes de um dispositivo específico"""
    if device_id not in devices:
        return jsonify({
            'success': False,
            'error': 'Dispositivo não encontrado'
        }), 404
    
    return jsonify({
        'success': True,
        'data': devices[device_id]
    }), 200

@app.route('/api/devices/<device_id>', methods=['PUT'])
def update_device(device_id):
    """Atualizar dispositivo"""
    if device_id not in devices:
        return jsonify({
            'success': False,
            'error': 'Dispositivo não encontrado'
        }), 404
    
    try:
        data = request.get_json()
        device = devices[device_id]
        
        # Atualizar campos permitidos
        if 'name' in data:
            device['name'] = data['name']
        if 'type' in data:
            device['type'] = data['type']
        if 'status' in data:
            device['status'] = data['status']
        
        device['updated_at'] = datetime.now().isoformat()
        
        return jsonify({
            'success': True,
            'message': 'Dispositivo atualizado',
            'data': device
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/devices/<device_id>', methods=['DELETE'])
def delete_device(device_id):
    """Deletar dispositivo"""
    if device_id not in devices:
        return jsonify({
            'success': False,
            'error': 'Dispositivo não encontrado'
        }), 404
    
    del devices[device_id]
    
    return jsonify({
        'success': True,
        'message': 'Dispositivo removido'
    }), 200

# ==================== LOCATIONS ====================

@app.route('/api/locations', methods=['GET'])
def get_locations():
    """Listar histórico de localizações"""
    device_id = request.args.get('device_id')
    limit = int(request.args.get('limit', 100))
    
    if device_id:
        # Filtrar por dispositivo
        filtered = [loc for loc in locations.values() 
                   if loc.get('device_id') == device_id]
        data = sorted(filtered, key=lambda x: x['timestamp'], reverse=True)[:limit]
    else:
        data = sorted(locations.values(), 
                     key=lambda x: x['timestamp'], reverse=True)[:limit]
    
    return jsonify({
        'success': True,
        'count': len(data),
        'data': data
    }), 200

@app.route('/api/locations', methods=['POST'])
def create_location():
    """Registrar nova localização"""
    try:
        data = request.get_json()
        
        # Validar dados obrigatórios
        required = ['device_id', 'latitude', 'longitude']
        if not data or not all(k in data for k in required):
            return jsonify({
                'success': False,
                'error': f'{required} são obrigatórios'
            }), 400
        
        location_id = f"{data['device_id']}_{datetime.now().timestamp()}"
        
        location = {
            'id': location_id,
            'device_id': data.get('device_id'),
            'latitude': data.get('latitude'),
            'longitude': data.get('longitude'),
            'accuracy': data.get('accuracy', 0),
            'signal_strength': data.get('signal_strength', -100),
            'timestamp': datetime.now().isoformat(),
            'source': data.get('source', 'gps')
        }
        
        locations[location_id] = location
        
        # Atualizar last_seen do dispositivo
        if data['device_id'] in devices:
            devices[data['device_id']]['last_seen'] = datetime.now().isoformat()
        
        return jsonify({
            'success': True,
            'message': 'Localização registrada',
            'data': location
        }), 201
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/locations/<location_id>', methods=['GET'])
def get_location(location_id):
    """Obter localização específica"""
    if location_id not in locations:
        return jsonify({
            'success': False,
            'error': 'Localização não encontrada'
        }), 404
    
    return jsonify({
        'success': True,
        'data': locations[location_id]
    }), 200

# ==================== STATS ====================

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Obter estatísticas do sistema"""
    online_devices = sum(1 for d in devices.values() if d['status'] == 'online')
    
    return jsonify({
        'success': True,
        'data': {
            'total_devices': len(devices),
            'online_devices': online_devices,
            'total_locations': len(locations),
            'timestamp': datetime.now().isoformat()
        }
    }), 200

# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 'Endpoint não encontrado'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'success': False,
        'error': 'Erro interno do servidor'
    }), 500

# ==================== MAIN ====================

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    
    print(f"""
    ╔════════════════════════════════════╗
    ║       LSF-Net Backend Started       ║
    ╚════════════════════════════════════╝
    
    🚀 Server: http://localhost:{port}
    📡 API Docs: http://localhost:{port}/api/health
    🔧 Debug: {debug}
    
    Pressione CTRL+C para parar
    """)
    
    app.run(host='0.0.0.0', port=port, debug=debug)
