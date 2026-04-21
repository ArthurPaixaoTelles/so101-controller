# SO101 Controller

> PT-BR | English below

## 🇧🇷 Descrição

O **SO101 Controller** é um sistema de controle desenvolvido para interação com o braço robótico SO-101, com foco em aplicações educacionais, experimentais e de pesquisa em robótica.

O projeto fornece uma base modular para controle de atuadores e comunicação com hardware, de modo a facilitar a manipulação das juntas do braço robótico. 

---

## 🎯 Objetivos

- Controlar o braço robótico SO-101
- Facilitar testes e prototipagem rápida
- Servir como base para teleoperação, ML/RL e automação

---

## ⚙️ Funcionalidades

- Interface de controle para atuadores
- Abstração de hardware
- Estrutura modular
---

## 📦 Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- Python 3.8+
- Node.js 16+ (inclui npm)
- Git

Opcional:
- Ambiente virtual Python (venv)

## 🚀 Instalação

```bash
git clone https://github.com/ArthurPaixaoTelles/so101-controller.git
cd so101-controller
cd backend
# (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\\Scripts\\activate  # Windows
pip install -r requirements.txt

```

---

## ▶️ Uso

```bash
"PARA ABRIR O SIMULADOR" MUJOCO_VIEWER=true uvicorn main:app --reload
só o back: uvicorn main:app --reload
cd ..
cd frontend
npm start

---

# 🇺🇸 English Version

## Description

**SO101 Controller** is a control system designed to interface with the SO-101 robotic arm for research and educational purposes.

---

## Installation

```bash
git clone https://github.com/ArthurPaixaoTelles/so101-controller.git
cd so101-controller
pip install -r requirements.txt
```

---

## Usage

```bash
python main.py
```