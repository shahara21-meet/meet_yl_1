encoder_caesar = {'a':'d','b':'e','c':'f','d':'g','e':'h','f':'i','g':'j','h':'k','i':'l','j':'m','k':'n','l':'o','m':'p','n':'q','o':'r','p':'s','q':'t','r':'u','s':'v','t':'w','u':'x','v':'y','w':'z','x':'a','y':'b','z':'c'}

def encode_string (x):
	for i in range (len(x)):
		if x[i] in encoder_caesar:
			x[i] = encoder_caesar[x[i]]

	return x

coded_word ='meet'
encoded_word=encode_string(coded_word)
print(encoded_word)
