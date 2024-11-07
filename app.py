from flask import Flask, render_template, request, jsonify
from datetime import datetime
from main import create_agent, process_message

app = Flask(__name__)
agent = create_agent()

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
    
    # Get response from agent
    result = process_message(agent, message)
    
    # Update metrics and state
    metrics['chat_sessions'] += 1
    analyst_state['current_focus'] = result['current_focus']
    analyst_state['confidence_level'] = result['confidence_level']
    analyst_state['processing_mode'] = result['processing_mode']
    
    return jsonify({
        'response': result['response'],
        'metrics': metrics,
        'analyst_state': analyst_state
    })

if __name__ == '__main__':
    app.run(debug=True)
