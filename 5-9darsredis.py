import redis

con = redis.Redis(host='localhost', port=6379, db=0)

# 1 - vazifa

# con.set('first_name', 'Nematjon')
# ism = con.get('first_name')
# print(str(ism, 'utf-8'))

# 2 - vazifa

# con.setnx('last_name', 'Rasulov')
# familiya = con.get('last_name')
# print(str(familiya, 'utf-8'))

# 3 - vazifa

# con.setex('age', 40, '22')
# yosh = con.get('age')
# print(str(yosh, 'utf-8'))

# 4 - vazifa

# con.getset('last_name', 'Qodirov')
# ism1 = con.get('last_name')
# print(str(ism1, 'utf-8'))

# 5 - vazifa

# con.set('age', 22)
# con.incr('age')
# yosh = con.get('age')
# print(str(yosh, 'utf-8'))
#
# con.incrby('age', 12)
# yosh = con.get('age')
# print(str(yosh, 'utf-8'))

# 6 - vazifa

# con.decr('age')
# yosh = con.get('age')
# print(str(yosh, 'utf-8'))
#
# con.decrby('age', 7)
# yosh = con.get('age')
# print(str(yosh, 'utf-8'))

# 7 - vazifa

# print(con.ttl('age'))

# print(con.exists('age'))

# 8 - vazifa

# con.mset({'address': 'Margilan', 'phone_number': '+998905825448'})
# info = con.mget(['address', 'phone_number'])
# for i in info:
#     print(str(i, 'utf-8'))

# 9 - vazifa

# con.append('address', '671')
# manzil = con.get('address')
# print(str(manzil, 'utf-8'))

# 10 - vazifa

# nomer = con.getrange('phone_number', 6, 12)
# print(str(nomer, 'utf-8'))

# 11 - vazifa

# con.setrange('address', 8, '377')
# manzil = con.get('address')
# print(str(manzil, 'utf-8'))

# 12 - vazifa

# manzil = con.get('address')
# print(manzil)
#
# con.delete('address')
# manzil = con.get('address')
# print(manzil)

# 13 - vazifa

# nomer = con.getset('phone_number', '5825448')
# print(str(nomer, 'utf-8'))
#
# nomer1 = con.get('phone_number')
# print(str(nomer1, 'utf-8'))

# 14 - vazifa

# print(con.strlen('first_name'))

# 15 - vazifa

# result = con.set('address', 'Fergana', nx=True)

# 16 - vazifa

# ism = con.getset('last_name', 'Rasulov')
# print(f"Eski qiymat: {ism.decode()}")

# 17 - vazifa

# con.set('mevalar', 'olma,gilos,xurmo,uzum')
# mevalar = str(con.get('mevalar'), 'utf-8')
# list_mevalar = mevalar.split(',')
# print(list_mevalar)

# 18 - vazifa

# type1 = con.type('first_name')
# print(str(type1, 'utf-8'))

# 19 - vazifa

# kalitlar = con.keys()
# for i in kalitlar:
#     print(str(i, 'utf-8'))

con.close()