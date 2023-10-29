# kathan
Full Stack django website using custom verson Bhashini API to convert to and fro all the Indian languages

For using its backend api send POST request to "http://127.0.0.1:8000/scaler/translate"
with data as: 
data = {
        "source_language": <INTEGER>,
        "content": <STRING>,
        "target_language": <INTEGER>
}<br/>
<h2>lanuage code</h2>
<li> Tamil (ta) : 1 </li>
<li>Telugu (te) : 2 </li>
<li>Hindi (hi) : 3</li>
<li>Malayalam (ml) : 4</li>
<li>Marathi (mr) : 5</li>
<li>Bengali (bn) : 6</li>
<li>Assamese (as) : 7</li>
<li>Gujarati (gu) : 8</li>
<li>Kannada (kn) : 9</li>
<li>Oriya (or) : 10</li>
<li>Punjabi (pa) : 11</li>
