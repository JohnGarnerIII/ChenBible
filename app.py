from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <body>
        <h1 style="text-align:center;">Chen Bible</h1>

        <p style="text-align:center;"> In the early days, in the realm of Dota, there arose a shepherd named Chen, the Holy Knight. He was not a man of swords or shields, but a man of faith and creatures, a true shepherd of the wild. </p>
        <p style="text-align:center;"> Chen was blessed with the power of Penitence, a divine touch that softens the hearts of his foes, causing them to falter in their steps and become susceptible to the strikes of the faithful. </p>
        <p style="text-align:center;"> He was graced with the Divine Favor, a blessing that increased the vitality of his allies and could call them from far-off lands to his side, mirroring the way he was called to service. </p>
        <p style="text-align:center;"> His greatest gift was the Holy Persuasion. With this power, Chen could sway the hearts of the beasts of the land, turning them from wild and untamed creatures into loyal companions. He guided them with a tender hand and a firm resolve, leading his unlikely congregation in the pursuit of righteousness. </p>
        <p style="text-align:center;"> Finally, with a compassionate heart as his guide, Chen was gifted with the Hand of God, the ultimate testament to his faith. With this divine power, he could mend the wounds of his brethren, no matter how far apart they may be. </p>
        <p style="text-align:center;"> Chen roamed the fields and forests, a beacon of light amidst the chaos of battle. His was not a path of violence, but of guidance and healing. In the trials of Dota, he stood not as a warrior, but as a holy knight, a testament to the power of faith and the strength of unity. </p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
