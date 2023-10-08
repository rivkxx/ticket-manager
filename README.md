<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Virtual Charity Event Ticket Manager</title>
</head>

<body>

    <h1>Virtual Charity Event Ticket Manager</h1>

    <p>Welcome to the Virtual Charity Event Ticket Manager, a Python-based application for managing tickets for your
        virtual charity event stream. This simple web application allows you to sell tickets, mark them as used, and
        keep track of attendees.</p>

    <h2>Features</h2>

    <ul>
        <li><strong>Sell Tickets:</strong> Add new attendees by providing their name and email address.</li>
        <li><strong>Manage Tickets:</strong> View the list of available tickets and mark them as used once attendees
            join the event.</li>
        <li><strong>Database:</strong> Uses SQLite to store ticket information securely.</li>
        <li><strong>Web Interface:</strong> Provides a user-friendly web interface to interact with the ticketing
            system.</li>
    </ul>

    <h2>Prerequisites</h2>

    <p>Make sure you have Python and Flask installed on your system. You can install Flask using the following
        command:</p>

    <pre><code>pip install flask</code></pre>

    <h2>Getting Started</h2>

    <ol>
        <li><strong>Clone the repository:</strong></li>
        <pre><code>git clone &lt;repository-url&gt;</code></pre>
        <pre><code>cd virtual-charity-event-ticket-manager</code></pre>
        <li><strong>Initialize the Database:</strong></li>
        <p>Run the <code>init_db.py</code> script to set up the SQLite database:</p>
        <pre><code>python init_db.py</code></pre>
        <li><strong>Run the Application:</strong></li>
        <p>Start the Flask application:</p>
        <pre><code>python app.py</code></pre>
        <p>The application will be accessible at <code>http://localhost:5000</code> in your web browser.</p>
    </ol>

    <h2>Usage</h2>

    <ul>
        <li>Visit <code>http://localhost:5000</code> in your browser to access the ticket manager.</li>
        <li>Sell new tickets by providing the attendee's name and email address.</li>
        <li>Mark tickets as used once attendees join the virtual charity event.</li>
    </ul>

    <h2>Contributing</h2>

    <p>If you have suggestions or found a bug, please open an issue. Contributions are welcome!</p>

    <h2>License</h2>

    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>

</html>
