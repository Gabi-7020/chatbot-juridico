from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

base_conhecimento = {
    "home_office": {
        "keywords": ["home office", "trabalho remoto", "teletrabalho", "trabalhar casa", "remoto"],
        "resposta": "🏠 HOME OFFICE E TRABALHO REMOTO:\n\n• Empresa deve fornecer equipamentos ou pagar auxílio\n• Horário de trabalho deve ser respeitado (mesmo em casa)\n• Direito à desconexão: não precisa responder fora do horário\n• Energia elétrica e internet podem ser ressarcidas\n• Acidentes em casa durante trabalho = acidente de trabalho\n• Reuniões por videoconferência não podem ser gravadas sem consentimento\n\n⚠️ IMPORTANTE: Tudo deve estar no contrato de trabalho ou acordo coletivo."
    }
}

def encontrar_resposta(mensagem):
    mensagem = mensagem.lower()
    for categoria, dados in base_conhecimento.items():
        for keyword in dados["keywords"]:
            if keyword in mensagem:
                return dados["resposta"]
    return "🤖 Desculpe, não encontrei uma resposta. Tente reformular sua pergunta."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    mensagem_usuario = request.json.get('message', '')
    if not mensagem_usuario:
        return jsonify({'response': 'Por favor, digite sua pergunta.'})
    resposta = encontrar_resposta(mensagem_usuario)
    return jsonify({'response': resposta})

if __name__ == '__main__':
    app.run(debug=True)
