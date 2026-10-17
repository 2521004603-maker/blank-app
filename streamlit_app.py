import streamlit as st

st.set_page_config(page_title="Quản Lý Quán Trà Sữa", page_icon="🧋")

st.title("🧋 Phần Mềm Quản Lý Quán Trà Sữa")
st.write("Chào mừng bạn đến với hệ thống gọi món trực tuyến!")

# Menu quán
menu = {
    "Trà sữa trân châu đường đen": 30000,
    "Trà sữa matcha": 35000,
    "Hồng trà đào": 25000,
    "Sữa tươi trân châu đường đen": 32000,
}

st.subheader("📋 Menu Đồ Uống")
selected_item = st.selectbox("Chọn món:", list(menu.keys()))
quantity = st.number_input("Số lượng:", min_value=1, value=1)

if st.button("Đặt món ngay"):
  total = menu[selected_item] * quantity
  st.success(
      f"Đã gọi thành công {quantity} {selected_item}! Tổng tiền: {total:,} VNĐ"
  )
