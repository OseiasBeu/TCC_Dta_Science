from googletrans import Translator

detector = Translator(service_urls=['translate.googleapis.com'])

string  = 'ODEIO'
# 'Porr Fmu eu te odeio, enfia essas aulas "híbridas" presenciais no seu c*...na moral EU NÃO POSSO IR PQ AGR MORO EM… https://t.co/42Cdld2fDX'
frase2 =detector.translate(string,dest='en')
dec_lan = detector.detect(string)

print(type(dec_lan))
print(dec_lan.lang)
print(frase2.text)

from textblob import TextBlob
testimonial = TextBlob(frase2.text)
print(testimonial.sentiment)