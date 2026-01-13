import json
import os
#====== update data ===============
def load_data(filename="datasinhvien.json"):
    if not os.path.exists(filename):
        return {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f) 
            data_converted = {int(k): v for k, v in data.items()}
            return data_converted
    except json.decoder.JSONDecodeError:
        return{}
    except Exception as e:
        return {}   
    
 #======== save data==========   
def save_data(thong_tin_sv, filename="datasinhvien.json"):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(thong_tin_sv, f, ensure_ascii=False, indent=4)
        print(">> Đã lưu dữ liệu vào file thành công!")
    except Exception as e:
        print(f"Có lỗi khi lưu file: {e}")

thong_tin_sv=load_data("datasinhvien.json")
"""
có định dạng : 
   masv:{name,date of birth,diem}
các thông tin của sv:
name
masv
date of birth 
diem( d1, d2)

"""

def check_masv(thon_tin_sv) -> int:   # cập  nhật mã sinh viên lớn nhất#
    masv=0
    if len(thong_tin_sv)==0: masv=0
    else: 
        masv=max(thong_tin_sv.keys())
    return masv

  #======== thêm sinh viên mới(cn1)===============
def add_sv(thong_tin_sv):
    """cập nhật masv khi thêm 1 sinh viên mới """
    
    masv=check_masv(thong_tin_sv)+1
    name=input("nhập tên của sinh viên:")
    date=input("nhập ngày tháng năm sinh theo dạng (ddmmyyyy):")
    try:
        diem=list(map(float, input("nhập điểm của sinh viên với định dạng ( hp1 , hp2)").split(",")))
    except ValueError:
        print("lỗi nhập điểm! sẽ gán điểm mặc định là 0.0 , 0.0")
        diem=[0.0, 0.0]
    thong_tin_sv[masv]={"name":name,"date of birth":date, "diem":diem}
    save_data(thong_tin_sv)
    print("_"*30)
    
 #========hiện thị tất cả=============================
def show_all(thong_tin_sv):
    for k,v in thong_tin_sv.items():
        print(f"mã sinh viên: {k}  : {v}")
    print("_"*30)
    
   #============ tìm kiếm thông tin của sinh viên(cn2)======================
def find(thong_tin_sv):
    tempt=input("điền họ và tên sinh viên:")
    count=1
    try:
        for i in thong_tin_sv:
            if thong_tin_sv[i]["name"]==tempt:
                print(f"{count} . masv:{i+1}-{thong_tin_sv[i]}")
            count+=1
    except Exception:
        print("không tồn tại!")
    print("_"*30)


    # ==========chỉnh sửa thông tin của sinh viên====================== 
def modification(thong_tin_sv):
    print("""
          CHỈNH SỬA THÔNG TIN CỦA SINH VIÊN""")
    ma_sv=int(input("mã sinh viên:"))
    if ma_sv not in thong_tin_sv:
        print("mã sinh viên không tồn tại!")
        return 
    print("thông tin của sinh viên:")
    print(thong_tin_sv[ma_sv])
    try:
        new_score1=float(input("nhập điểm muốn sửa(thành phần 1):"))
        new_score2=float(input("nhập điểm muốn sửa (thành phần 2):"))
        new_name=(input("chỉnh sửa tên mới:"))
        new_dateofbirth=input("chỉnh sửa ngày sinh theo định dạng ddmmyyyy:")
        # cập nhật thông tin
        if new_name!=None: thong_tin_sv[ma_sv]["name"]=new_name
        if new_dateofbirth != None: thong_tin_sv[ma_sv]["date of birth"]=new_dateofbirth
        if new_score1 != None and new_score2!= None: thong_tin_sv[ma_sv]["diem"]=[new_score1,new_score2]
    
        save_data(thong_tin_sv)
    except ValueError:
        print("LỖI: bạn đã nhập sai định dạng ")
    print("_"*30)


    #================= phân loại sinh viên(cn3)=====================
def plsv(thong_tin_sv):
    #tạo hàm# 
    def plname(thong_tin_sv):# phân loại theo tên ( hiện thị các tên thỏa mãn yêu cầu)
        tempt=input("nhập chữ cái đầu của tên:")
        for i in thong_tin_sv.keys():
            if tempt.upper() in thong_tin_sv[i]["name"]:
                print(thong_tin_sv[i])
    
    def plhigherscore(thong_tin_sv):# phân loại theo lớn hơn điểm thành phần ( phân loại theo tp1 or tp2 or cả 2)
        tp1=float(input("nhập điểm thành phần 1:"))
        tp2=float(input("nhập điểm thành phần 2:"))
        if tp1 != None and tp2 == None:
            for key in thong_tin_sv.keys():
                if thong_tin_sv[key]["diem"][0]>= tp1:
                    print(thong_tin_sv[key])
        elif tp1==None and tp2!=None:
            for key in thong_tin_sv.keys():
                if thong_tin_sv[key]["diem"][1]>=tp2:
                    print(thong_tin_sv[key])
        elif tp1!=None and tp2!=None:    
            for key in thong_tin_sv.keys():
                if thong_tin_sv[key]["diem"][1]>=tp2 and thong_tin_sv[key]['diem'][0]>=tp1:
                    print(thong_tin_sv[key])
    
    def pllowerscore(thong_tin_sv):# phân loại theo nhỏ hơn điểm thành phần ( phân loại theo tp1 or tp2 or cả 2)
        tp1=float(input("nhập điểm thành phần 1:"))
        tp2=float(input("nhập điểm thành phần 2:"))
        if tp1 != None and tp2 == None:
            for key in thong_tin_sv.keys():
                if thong_tin_sv[key]["diem"][0]<= tp1:
                    print(thong_tin_sv[key])
        elif tp1==None and tp2!=None:
            for key in thong_tin_sv.keys():
                if thong_tin_sv[key]["diem"][1]<=tp2:
                    print(thong_tin_sv[key])
        elif tp1!=None and tp2!=None:    
            for key in thong_tin_sv.keys():
                if thong_tin_sv[key]["diem"][1]<=tp2 and thong_tin_sv[key]['diem'][0]<=tp1:
                    print(thong_tin_sv[key])
        
    #thực hiện hàm#    
    print("""
          LỰA CHỌN CÁCH PHÂN LOại:
          1 -> phân loại theo tên
          2 -> phân loại theo điểm thành phần lớn hơn
          3 -> phân loại theo điểm thành phần nhỏ hơn
          quit -> dừng phân loại""") 
        
        
    starting=input("nhập yêu cầu của bạn:")
        
    while starting != 'quit':
            if starting =='1':
                plname(thong_tin_sv)
                print("_"*30)
                starting=input("nhập yêu cầu của bạn:")
            elif starting=='2':
                plhigherscore(thong_tin_sv)
                print("_"*30)
                starting=input("nhập yêu cầu của bạn:")
            elif starting=='3':
                pllowerscore(thong_tin_sv)
                print("_"*30)
                starting=input("nhập yêu cầu của bạn:")
    print("_"*30)

  #==========tính điểm trung bình(cn4)=================== 
def tinh_diem_trung_binh(thong_tin_sv):
    sum1=0
    sum2=0
    for i in thong_tin_sv.keys():
        sum1+=thong_tin_sv[i]["diem"][0]/len(thong_tin_sv)
        sum2+=thong_tin_sv[i]["diem"][1]/len(thong_tin_sv)
    print(f"điểm trung bình của điểm thành phần 1 là :{sum1:.2f}")
    print(f"điểm trung bình của điểm thành phần 2 là :{sum2:.2f}")

    print("_"*30)    
        
        
   #===========xóa thông tin sinh viên(cn5)=================
def delete_information(thong_tin_sv):
    try:
        ma_sv=int(input("nhập mã sinh viên:"))
        del thong_tin_sv[ma_sv]
    except Exception:
        print("không có dữ liệu!")
    save_data(thong_tin_sv)
    
   #============ cộng điểm cộng(cn6)==================
def pluss_score(thong_tin_sv):
    tempt=list(map(int,input("nhập các mã số sinh viên:").split()))
    
    def plustp1(thong_tin_sv,tempt):# cộng điểm thành phần 1
        tp1=float(input("điểm cộng thành phần 1:"))
        for i in tempt:
            thong_tin_sv[i]["diem"][0]+=tp1
            if thong_tin_sv[i]["diem"][0]>10.0:
                thong_tin_sv[i]["diem"][0]=10.0
    
    def plustp2(thong_tin_sv,tempt):# cộng điểm thành phần 2
        tp2=float(input("điểm cộng thành phần 2:"))
        for i in tempt:
            thong_tin_sv[i]["diem"][1]+=tp2
            if thong_tin_sv[i]["diem"][1]>10.0:
                thong_tin_sv[i]["diem"][1]=10.0
    print("""
          1-> cộng điểm thành phần 1
          2-> cộng điểm thành phần 2""")
    # thực thi chương trình#
    n=int(input("lựa chọn cộng điểm 1 or 2 : "))
    while n!=1 and n!=2:
        n=int(input("lựa chọn lại cộng điểm 1 or 2 (lưu ý nhớ định dạng đúng:"))
    if n==1:
        plustp1(thong_tin_sv,tempt)
    elif n==2:
        plustp2(thong_tin_sv,tempt)
    
    save_data(thong_tin_sv)
    
    print("_"*30)
#code giao diện tương tác#
# ================== MENU ==================

def main_menu():
    print("""
=============================
  QUẢN LÍ SINH VIÊN
=============================
1. Thêm sinh viên
2. Tìm sinh viên
3. Sửa thông tin
4. Phân loại sinh viên
5. Tính điểm trung bình
6. Xóa sinh viên
7. Cộng điểm
8. Hiển thị tất cả
0. Thoát
=============================
""")
    while True:
  
        ch = input("Chọn: ")

        if ch == "1":
            add_sv(thong_tin_sv)
        elif ch == "2":
            find(thong_tin_sv)
        elif ch == "3":
            modification(thong_tin_sv)
        elif ch == "4":
            plsv(thong_tin_sv)
        elif ch == "5":
            tinh_diem_trung_binh(thong_tin_sv)
        elif ch == "6":
            delete_information(thong_tin_sv)
        elif ch == "7":
            pluss_score(thong_tin_sv)
        elif ch == "8":
            show_all(thong_tin_sv)
        elif ch == "0":
            print("👋 Thoát chương trình")
            break
        else:
            print("❌ Lựa chọn không hợp lệ")


# ================== START ==================

if __name__ == "__main__":
    main_menu()
#code giao diện tương tác#
save_data(thong_tin_sv,"datasinhvien.json")

