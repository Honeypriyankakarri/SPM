from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
def token(rollno,seconds):
     s=Serializer('h&YwehiGfty&',seconds)
     return s.dumps({'user':rollno}).decode('utf-8')
    
