import speedtest
from datetime import datetime
import time
now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')  # format as 'YYYY-MM-DD HH:MM:SS'
hour = now.hour
with open("spedtest.txt", "a") as f:
            f.write(f"{formatted_date}: \n")
            st = speedtest.Speedtest()
            upload_speed = st.upload()
            download_speed = st.download() 
            f.write(f"  Download Speed: {download_speed / 1_000_000:.2f} Mbps\n")
            f.write(f"  Upload Speed: {upload_speed / 1_000_000:.2f} Mbps\n")