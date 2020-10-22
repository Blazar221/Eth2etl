def safe_url_base64(base64):
	return base64.replace('+', '-').replace('/', '_')


def db_fit(root):
	return root.replace('=','')


