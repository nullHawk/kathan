# kathan
Full Stack django website using custom verson Bhashini API to convert to and fro all the Indian languages

For using its backend api send POST request to "http://127.0.0.1:8000/scaler/translate"
with data as: 
data = {
        "source_language": <INTEGER>,
        "content": <STRING>,
        "target_language": <INTEGER>
}

