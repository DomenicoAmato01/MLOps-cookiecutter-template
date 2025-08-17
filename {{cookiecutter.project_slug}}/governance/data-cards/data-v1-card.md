# Data Card: [Nome del Dataset, es. DRIVE]

> Questa Data Card fornisce dettagli cruciali sul dataset utilizzato per il training e la valutazione dei modelli.

---

## 1. Motivazione e Composizione

- **Scopo:** Perché è stato creato questo dataset?
  - [Es. Per fornire un gold standard per la segmentazione dei vasi sanguigni nella retina per studi sulla retinopatia diabetica.]
- **Autori/Creatori:** [Chi ha creato e mantiene il dataset?]
- **Fonte dei Dati:** [Da dove provengono i dati? Es. Immagini raccolte da uno screening di 400 soggetti.]

---

## 2. Processo di Raccolta

- **Periodo di Raccolta:** [In che periodo sono stati raccolti i dati?]
- **Metodologia di Campionamento:** [Come sono stati selezionati i partecipanti/le immagini?]
- **Dispositivi Utilizzati:** [Es. Fotocamera fundus Canon CR5 non midriatica.]

---

## 3. Struttura e Contenuto

- **Formato dei Dati:** [Es. Immagini TIFF, maschere GIF.]
- **Numero di Istanze:** [Es. 40 immagini (20 per training, 20 per test).]
- **Processo di Annotazione/Etichettatura:**
  - [Chi ha etichettato i dati? Es. Due osservatori umani; un oftalmologo ha risolto le discordanze.]
  - [Qual era il protocollo di etichettatura?]

---

## 4. Distribuzione e Statistiche

- **Dati Demografici:** [Es. Età, genere, etnia dei soggetti, se disponibili e pertinenti.]
- **Caratteristiche delle Immagini:** [Es. Risoluzione (565x584 pixel), statistiche su luminosità e contrasto.]
- **Eventuali Dati Mancanti o Rumore:** [Sono presenti problemi noti con il dataset?]

---

## 5. Utilizzo Raccomandato e Limitazioni

- **Casi d'Uso Previsti:** [Es. Benchmarking di algoritmi di segmentazione, ricerca accademica.]
- **Considerazioni sulla Privacy:** [I dati sono anonimizzati? Quali misure sono state prese per proteggere la privacy?]
- **Bias Noti:** [Es. Il dataset è composto principalmente da soggetti di una specifica area geografica, il che potrebbe limitare la generalizzabilità.]
- **Licenza:** [Qual è la licenza d'uso? Es. Creative Commons, uso solo per ricerca.]

---

## 6. Manutenzione

- **Stato del Dataset:** [È ancora mantenuto? Vengono aggiunti nuovi dati?]
- **Come Citare:** [Fornire la citazione bibliografica corretta.]
- **Versione DVC del Dataset:** `[hash del dataset in DVC]`