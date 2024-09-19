import win32pdh
import time

def get_cpu_frequency():
    try:
        # Performance Counter für die CPU-Auslastung abfragen
        query_handle = win32pdh.OpenQuery()
        counter_handle = win32pdh.AddCounter(query_handle, r"\Prozessorinformationen(_Total)\% Prozessorleistung")

        # Abfrage starten
        win32pdh.CollectQueryData(query_handle)
        time.sleep(1)  # Kurze Verzögerung, um sicherzustellen, dass Daten gesammelt werden

        # Daten abrufen
        win32pdh.CollectQueryData(query_handle)
        _, value = win32pdh.GetFormattedCounterValue(counter_handle, win32pdh.PDH_FMT_DOUBLE)

        cpu_freq = (3700/100) * value

        #print(f"Prozessorfrequenz: {cpu_freq:.2f}")
        

    except Exception as e:
        print(f"Fehler: {e}")

    finally:
        if 'query_handle' in locals():
            win32pdh.CloseQuery(query_handle)
        return cpu_freq