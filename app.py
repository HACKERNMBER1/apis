

from flask import *

import random

app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/")

def Oh():

    azkr = ['اللهم أتمم عافيتك علي ونعمتك وسترك في الدنيا والآخرة.','اللهم أتمم عافيتك علي ونعمتك وسترك في الدنيا والآخرة.','اللهم أرني عجائب قدرتك في استجابة دعائي.'

        ,'لا حول ولا قوة إلا بالله العلي العظيم.','لا إله إلا أنت سبحانك إني كنت من الظالمين.',

            '‏﴿يا أَيُّهَا الَّذينَ آمَنُوا اذكُرُوا اللَّهَ ذِكرًا كَثيرًا﴾','‏"أمَّا السَّفينةُ وأمَّا الغُلامُ وأمَّا الجِدَارُ،  ‏اللهمَّ صبراً على ما لم نُحِطْ به خُبراً" 🤍',

            'أَكْثِرُوا مِنْ قَوْلِ : لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللَّهِ ، فَإِنَّهَا كَنْزٌ مِنْ كُنُوزِ الْجَنَّةِ',

            'ما أصاب المؤمن من هم ولا غم ولا حزن حتى الشوكة يشاكها إلا كفر الله من خطاياه، إنه الغفور الرحيم.',

            '‏"ولسُوف يعطيك ربك فترضَى"💎‏يارب هالرضَا.',

            'اللهم أفتح بيني وبين رزقي ونصيبي وسعادتي وتوفيقي فتحاً مبيناً وأنت خير الفاتحين.','وَمَا كَانَ اللَّهُ لِيُعَذِّبَهُمْ وَأَنتَ فِيهِمْ ۚ وَمَا كَانَ اللَّهُ مُعَذِّبَهُمْ وَهُمْ يَسْتَغْفِرُونَ (33)',

            '‏رَبِّ إِنِّي لِمَا أَنْزَلْتَ إِلَيَّ مِنْ خَيْر فَقِير .','اللهم إن كنت قد أذنبت ذنباً مسك عني رزقي وتوفيقي فإني استغفرك ربي حتى تغفر لي.',

            'ربّي عوضني خيرًا عن كل شيء انكسر بنفسي، وكل يأسٍ أصاب قلبي، ولا تجعل لي رجاء عند غيرك، اللهُم ارني الفرح بمُستقبلي، اللهُم سُر قلبي بفرحةٍ، تغنيني عن كل تعب، اللهُم عوضني بالأجمل، وأرح قلبي بما أنت أعلمُ به.'

            ]

    Az = random.choice(azkr)

    return Az

if __name__ == "__main__":

    app.run(debug=True)
