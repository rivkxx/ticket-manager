from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Function to add a new ticket to the database
def add_ticket(name, email):
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tickets (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()

# Function to get all available tickets
def get_available_tickets():
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tickets WHERE used = 0')
    tickets = cursor.fetchall()
    conn.close()
    return tickets

# Route to display available tickets and sell new tickets
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        add_ticket(name, email)
    tickets = get_available_tickets()
    return render_template('index.html', tickets=tickets)

# Route to mark a ticket as used
@app.route('/use_ticket/<int:ticket_id>')
def use_ticket(ticket_id):
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tickets SET used = 1 WHERE id = ?', (ticket_id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
