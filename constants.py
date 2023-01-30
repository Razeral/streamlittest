from enum import Enum, unique

# https://docs.python.org/3/library/enum.html#others
class StrEnum(str, Enum):
    pass
  
@unique
class UOBMerchants(StrEnum):
    MerchantList = ["8 Degrees Taiwanese Bistro","Aburi-EN Grand (Paragon)","Baker & Cook","Bee Cheng Hiang","Bones ‘N Slaw","BreadTalk","Canteen by Trapeze Rec. Club","Cellarbration","CHICHA San Chen","Co Chung","Chicken Claypot House","Famous Kitchen","Fatburger & Buffalo’s","Feng Tian Xiao Chu","Hard Rock Cafe","Hitoyoshi Ramen & Gril","Hitoyoshi Yoshi Sushi","Indian House","I.N.U Cafe & Boutique","Mr Coconut","Mun ZUk","Nam Kee Chicken Rice Restaurant","Patisserie G","Pazzion Cafe","Polar Puffs & Cakes","Potato Corner","Prince Kitchen","Qin Ji Rougamo","Q-WA Izakaya","Ramen Hitoyoshi","Starbucks","Tangmen Restaurant","Tian Tian You Yu","ToastBox","Wangzi Music Restaurant","Xiu Jie Shan Cheng Fish","Yuan Cuisine Group","Bincho at Hua Bee","Bincho at Min Jiang","Marguerite","Hortus","Kotuwa","Majestic Bay","Meatsmith Little India","Meatsmith Telok Ayer","Restaurant Majestic","Salted and Hung","Cold Storage","Giant","agnes B","Buf’d Nail Spa","bYSI","Crocodile","Delta Dental Surgeons","DermaCurate","EMW Physiotherapy & TCM","Fenjiu Flagship Store","Gordon Max","G-Star Raw","Guardian","Honey World","iRUN","King Koil & Ashley Homestores","Limited Edit Underground","Marco Nail Spa","Masculine Men Skincare","Miniso","MissFit","New Era","Optique Paris Miki","Osman Silk House","Pazzion","Perky Lash","Picota Nail Spa","Qoosh Nail Spa","Replay","Salivan Beauty Clinic","Sports Fashion","United Overseas Insurance","Winter Time","Western Corp","Yangyi Beauty and BodyCare","Cathay Cineplexes","City Tours"]
