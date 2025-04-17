<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Files to ZIP Converter</h1>
    <h2>Description</h2>
    <p>
        The <strong>Files to ZIP Converter</strong> is a Django-based web application that allows users to upload multiple files, which are then compressed into a single ZIP file. After conversion, the user can download the ZIP archive containing all the uploaded files. This tool is helpful for packaging and sharing multiple files quickly and efficiently.
    </p>
    <h2>Features</h2>
    <ul>
        <li><strong>Multiple File Upload:</strong> Upload one or more files through a web interface.</li>
        <li><strong>ZIP Compression:</strong> Automatically compress uploaded files into a ZIP archive.</li>
        <li><strong>Download ZIP:</strong> Download the resulting ZIP file after conversion.</li>
        <li><strong>Temporary Storage:</strong> Files are temporarily stored and deleted after download to maintain server hygiene.</li>
    </ul>
    <h2>Tech Stack</h2>
    <ul>
        <li><strong>Backend:</strong> Django, Python (zipfile module)</li>
        <li><strong>Frontend:</strong> HTML, CSS (optional JavaScript for progress)</li>
        <li><strong>Storage:</strong> In-memory or temporary file system</li>
    </ul>
    <h2>Requirements</h2>
    <p>To run this project locally, ensure the following:</p>
    <ul>
        <li>Python 3.x</li>
        <li>Django 5.x</li>
    </ul>
    <h2>Installation</h2>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone https://github.com/yourusername/files-to-zip-converter.git</code></pre>
        </li>
        <li>Navigate to the project directory:
            <pre><code>cd files-to-zip-converter</code></pre>
        </li>
        <li>Create and activate a virtual environment:
            <pre><code>python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate</code></pre>
        </li>
        <li>Install dependencies:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Run migrations:
            <pre><code>python manage.py migrate</code></pre>
        </li>
        <li>Start the development server:
            <pre><code>python manage.py runserver</code></pre>
        </li>
        <li>Open in browser:
            <pre><code>http://127.0.0.1:8000/</code></pre>
        </li>
    </ol>
    <h2>Usage</h2>
    <ol>
        <li>Visit the homepage where the upload form is displayed.</li>
        <li>Select multiple files using the file picker.</li>
        <li>Click the <strong>"Convert to ZIP"</strong> button.</li>
        <li>Wait for the server to process and generate the ZIP file.</li>
        <li>A download link/button will appear – click it to download your ZIP archive.</li>
    </ol>
    <h2>Note</h2>
    <p>
        Files are not stored permanently. They are deleted after conversion and download for security and storage management.
    </p>
</body>
</html>
