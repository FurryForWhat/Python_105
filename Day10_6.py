my_list = []
for number in range(100,401):
    my_list.append(number)

even_list =[]
odd_list= []
for number in range(100,401):
    if number%2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)
print(even_list)
print(odd_list)
#even listထဲမှာ 4နဲ့စားလို့ပြတ်တဲ့ကိန်းကို listထဲထည့်မယ်။ စားလို့မပြတ်တဲ့ကိန်းကို tupleထဲထည့်မယ်။
#odd list ထဲမှာ 23နဲ့စားလို့ပြတ်တဲ့ကိန်းကို tupleထဲထည့်မယ်။ မပြတ်ရင် listထဲထည့်မယ်။
#အဲ့ဒီ variable 4ခုကို for loop နဲ့ထုတ်ပြရမယ် ။ မတူရဘူး

#စာပိုဒ်တစ်ခုကိုယူပြီးတော့ vowels ဘယ်နှစ်လုံးပါလဲဆိုတာကို စစ်ရမယ်။