#function used to generate tests, in case I'll need more

def atbash_gen(plaintext: str) -> dict:
    alpha = 'AaBbCcDdEeFfGgHhIiJjKkLlMmnNoOpPqQrRsStTuUvVwWxXyYzZ'
    ciphertext = ''.join([alpha[51 - alpha.find(i)] if i.isalpha() else i for i in plaintext])
    
    return {'input': plaintext, 
            'answer': ciphertext}
