from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

def analyze_can_log(log_data):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": """You are an expert automotive CAN bus and network protocol analyzer. 
You understand CAN trace logs from Vector CANoe and Wireshark captures.
When given log data, you:
1. Identify message IDs and their likely purpose
2. Detect errors, anomalies, or unusual patterns
3. Highlight critical messages (errors, warnings, bus-off events)
4. Summarize what is happening on the network
5. Suggest possible root causes for any issues found
Use your knowledge of UDS, J1939, CAN protocols to give expert analysis."""},
            {"role": "user", "content": f"Analyze this CAN log:\n\n{log_data}"}
        ]
    )
    return response.choices[0].message.content

# Sample CAN trace log (similar to CANoe output)
sample_log = """
   0.000000  1  0CF00400x        Rx   d 8  FF FF FF FF FF FF FF FF
   0.005000  1  18FEDF00x        Rx   d 8  FA 12 00 FF FF FF FF FF
   0.010000  1  0CF00300x        Rx   d 8  FF FF 7D 00 FF FF FF FF
   0.015000  1  18FEE000x        Rx   d 8  00 00 00 00 FF FF FF FF
   0.020000  1  0CF00400x        Rx   d 8  FF FF FF FF FF FF FF FF
   0.025000  1  18FEDF00x        Rx   d 8  FA 13 00 FF FF FF FF FF
   0.030000  1  18EA00F9x        Rx   d 3  00 FE 18
   0.035000  1  18EAFF00x        Tx   d 3  B0 FE 00
   0.040000  1  18EB00F9x        Rx   d 8  10 1D 00 01 00 B0 FE 00
   0.045000  1  18EC00F9x        Rx   d 8  11 00 00 00 00 00 00 00
   0.050000  ErrorFrame
   0.055000  1  18FEE000x        Rx   d 8  FF FF FF FF FF FF FF FF
   0.060000  1  0CF00300x        Rx   d 8  FF FF 7E 00 FF FF FF FF
   0.065000  ErrorFrame
   0.070000  1  18FEDF00x        Rx   d 8  FB 13 00 FF FF FF FF FF
   0.075000  1  18EA00F9x        Rx   d 3  00 FE 18
   0.080000  BusOff
   0.085000  1  18EAFF00x        Tx   d 3  B0 FE 00
"""

print("Analyzing CAN log...\n")
print("=" * 60)
result = analyze_can_log(sample_log)
print(result)
print("=" * 60)