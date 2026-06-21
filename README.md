# LSF-Net – Localizador de Seres Físicos em Rede

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)]()

**Versão 1.0.0** - Sistema de localização de pessoas em rede com tecnologia de triangulação de sinais WiFi e Bluetooth.

> Em menos de 5 minutos você terá tudo rodando! 🎯

Desenvolvido com ❤️ por **IcaroLeite-Uarini-AM-Brasil**  
Licença MIT - Use livremente | Data: 2026-06-21

---

## 🚀 Quick Start

### Pré-requisitos
- Python 3.10+
- Docker (opcional)
- Git

### 1. Clone o repositório
```bash
git clone https://github.com/IcaroLeite-Uarini-AM-Brasil/LSF-Net.git
cd LSF-Net
```

### 2. Execute o setup automático
```bash
bash scripts/setup.sh
```

### 3. Inicie o sistema
```bash
# Desenvolvimento local
python backend/app.py

# Ou com Docker
docker-compose up -d
```

### 4. Acesse no navegador
```
http://localhost:5000
```

---

## 📋 Funcionalidades

- ✅ **Localização em Tempo Real** - Rastreie dispositivos WiFi e Bluetooth
- ✅ **Triangulação de Sinais** - Algoritmo de posicionamento avançado
- ✅ **Dashboard Web** - Interface responsiva e intuitiva
- ✅ **API REST** - Integração com terceiros
- ✅ **Histórico** - Registre todos os movimentos
- ✅ **Alertas** - Notificações em tempo real

---

## 📁 Estrutura do Projeto

```
LSF-Net/
├── backend/                 # API Python/Flask
│   ├── app.py              # Aplicação principal
│   ├── config.py           # Configurações
│   ├── models/             # Modelos de dados
│   ├── routes/             # Endpoints da API
│   └── utils/              # Funções utilitárias
├── frontend/               # Interface Web
│   ├── index.html          # Página principal
│   ├── css/                # Estilos
│   └── js/                 # JavaScript
├── deployment/             # Docker e produção
│   ├── Dockerfile
│   └── docker-compose.yml
├── docs/                   # Documentação técnica
│   ├── API.md
│   ├── INSTALLATION.md
│   └── ARCHITECTURE.md
├── scripts/                # Scripts utilitários
│   └── setup.sh           # Setup automático
└── tests/                  # Testes automatizados
```

---

## 🔧 Instalação Detalhada

### Via Script (Recomendado)
```bash
bash scripts/setup.sh
```

### Via Docker
```bash
docker-compose up -d
# Acesse em http://localhost:5000
```

### Via Python (Manual)
```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r backend/requirements.txt

# Executar
python backend/app.py
```

---

## 📚 Documentação

Consulte os arquivos na pasta `docs/` para:
- [Guia de Instalação Completo](docs/INSTALLATION.md)
- [Documentação da API](docs/API.md)
- [Arquitetura do Sistema](docs/ARCHITECTURE.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)
- [BOM - Bill of Materials](docs/BOM.md)

---

## 🧪 Testes

```bash
# Executar todos os testes
python -m pytest tests/ -v

# Testes com cobertura
pytest --cov=backend tests/
```

---

## 📡 API Endpoints

```
GET    /api/health          - Status da aplicação
GET    /api/devices         - Listar dispositivos
GET    /api/devices/:id     - Detalhes do dispositivo
POST   /api/devices         - Registrar novo dispositivo
GET    /api/locations       - Histórico de localizações
GET    /api/locations/:id   - Localização específica
```

Documentação completa: [docs/API.md](docs/API.md)

---

## 🐛 Troubleshooting

**Porta 5000 já em uso?**
```bash
# Linux/Mac
sudo lsof -i :5000
kill -9 <PID>

# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

**Erro de dependências?**
```bash
pip install --upgrade -r backend/requirements.txt
```

Para mais: [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)

---

## 🤝 Contribuindo

Contributions são bem-vindas! Por favor:

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📝 Roadmap

- [ ] v1.1 - Suporte a LoRaWAN
- [ ] v1.2 - Integração com Google Maps
- [ ] v1.3 - App Mobile (React Native)
- [ ] v2.0 - Machine Learning para previsão

---

## 📄 Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 📞 Suporte

- 📧 Email: icaro@example.com
- 💬 Issues: [GitHub Issues](https://github.com/IcaroLeite-Uarini-AM-Brasil/LSF-Net/issues)
- 📖 Docs: [Documentação Completa](docs/)

---

**Última atualização:** 21 de junho de 2026 ✨
