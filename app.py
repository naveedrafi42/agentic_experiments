from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Simulated metrics data - in a real app, this would come from a database
metrics = {
    'analyses_completed': 0,
    'insights_generated': 0,
    'chat_sessions': 0
}

# Simulated analyst state
analyst_state = {
    'current_focus': 'Ready to analyze data',
    'confidence_level': 95,
    'processing_mode': 'Active listening'
}

@app.route('/')
def home():
    return render_template('index.html', 
                         metrics=metrics,
                         analyst_state=analyst_state)

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get('message', '')
    # Simulate analyst response
    response = f"I understand your query: '{message}'. Let me analyze that..."
    
    # Update metrics
    metrics['chat_sessions'] += 1
    
    return jsonify({
        'response': response,
        'metrics': metrics,
        'analyst_state': analyst_state
    })

if __name__ == '__main__':
    app.run(debug=True)
