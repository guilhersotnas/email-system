# Sistema Distribuído de Envio de Emails

Projeto desenvolvido para a disciplina de Microsserviços utilizando Docker, Flask, RabbitMQ, ZooKeeper e MailHog.

## 📌 Objetivo

Desenvolver um sistema distribuído de envio de emails corporativos utilizando arquitetura de microsserviços, comunicação assíncrona com RabbitMQ e containers Docker orquestrados com Docker Compose.

---

# 👨‍💻 Integrantes

- Bianca Nicolli Celso dos Santos
- Gabriella Silvestre Annunciato
- Giovanna Silvestre Annunciato
- Guilherme dos Santos Ferreira

## 🎓 Instituição

FATEC Antonio Russo  
São Caetano do Sul  
AMS ADS - 2º Semestre

---

# 🛠 Tecnologias Utilizadas

- Docker
- Docker Compose
- Python
- Flask
- RabbitMQ
- ZooKeeper
- MailHog
- smtplib
- HTML
- CSS
- JavaScript

---

# 🏗 Arquitetura do Sistema

O sistema é composto pelos seguintes microsserviços:

| Serviço | Função |
|---|---|
| Frontend | Interface web para envio de emails |
| Backend | API responsável por publicar mensagens no RabbitMQ |
| Consumer | Consome mensagens da fila e envia emails |
| RabbitMQ | Broker de mensageria |
| ZooKeeper | Gerenciamento de configurações distribuídas |
| MailHog | Servidor SMTP de testes |

---

# 📂 Estrutura do Projeto

```bash
email-system/
│
├── backend/
├── frontend/
├── consumer/
├── docker-compose.yml
└── README.md
