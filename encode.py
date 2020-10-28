# Base64 format contains characters like '+' and '/', but net url don't allow their appearance. Instead, url allows the safe_url_base64 format and can automatically recognize the special converted characters in it.
def safe_url_base64(base64):
	return base64.replace('+', '-').replace('/', '_')


# Mysql database don't allow the appearance of '=' in data, so before saving it, '=' at the end of the string should be eliminated.
def db_parse(root):
	return root.replace('=','')


