# โค้ดสร้างเว็บแอปด้วย Streamlit (เอาไปเซฟชื่อ app.py)
import streamlit as st
import yfinance as yf
import pandas as pd

st.title("🚀 Radar Bot ของ Clack & Cook45")
st.write("เว็บส่วนตัวสำหรับสแกนกราฟและสัญญาณเทรด")

# ให้มึงพิมพ์ชื่อหุ้นที่อยากดูได้เลย
ticker = st.text_input("พิมพ์ชื่อย่อหุ้นที่มึงอยากดู (เช่น SPY, AAPL, BRK-B)", "SPY")

if st.button("สแกนกราฟเดี๋ยวนี้!"):
    with st.spinner('บอทกำลังดูดข้อมูล...'):
        stock = yf.Ticker(ticker)
        df = stock.history(period="1y")
        
        if not df.empty:
            # คำนวณเส้นสายต่างๆ
            df['SMA_50'] = df['Close'].rolling(window=50).mean()
            df['SMA_200'] = df['Close'].rolling(window=200).mean()
            
            cp = df['Close'].iloc[-1]
            st.success(f"🎯 ราคาล่าสุดของ {ticker}: ${cp:,.2f}")
            
            # วาดกราฟโชว์บนเว็บแม่งเลย
            st.write("📊 กราฟราคาพร้อมเส้นแบ่งนรกสวรรค์ (SMA50 & SMA200)")
            st.line_chart(df[['Close', 'SMA_50', 'SMA_200']])
            
            st.info("💡 ข้อแนะนำ: ถ้าเส้นราคา (สีน้ำเงิน) อยู่ใต้เส้นอื่นๆ แปลว่าขาลง ห้ามซื้อสัส!")
            
        else:
            st.error("❌ หาหุ้นไม่เจอเว้ย พิมพ์ชื่อผิดป่าวสัส!")
