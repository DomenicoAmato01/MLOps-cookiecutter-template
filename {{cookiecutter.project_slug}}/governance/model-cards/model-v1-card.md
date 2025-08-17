# Model Card: {{ cookiecutter.project_name }} - Model v1.0

> Questa Model Card fornisce informazioni contestuali e di trasparenza sul modello di segmentazione.

---

## 1. Dettagli del Modello

- **Nome Modello:** ML Model
- **Versione:** 1.0
- **Sviluppato da:** {{ cookiecutter.author_name }}
- **Data:** {{ now() | strftime('%Y-%m-%d') }}
- **Tipo di Modello:** Architettura ML
- **Informazioni di Contatto:** [Email o team di contatto]

---

## 2. Utilizzo Previsto

- **Uso Primario:** 
- **Utenti Target:** 
- **Casi d'Uso Fuori Scopo (Out-of-Scope):**
  - **NON** 

---

## 3. Dati di Training

- **Dataset Utilizzati:** [Nome del dataset, es. DRIVE, CHASE_DB1]. Link alla relativa **Data Card**: `../data_cards/dataset-v1-card.md`.
- **Dati di Preprocessing:** Le immagini sono state normalizzate [specificare come] e ridimensionate a {{ cookiecutter.img_size }} pixel. È stata applicata data augmentation (rotazioni, flip).
- **Variabili Demografiche/Sensibili:** Il dataset di training ha la seguente distribuzione: [Es. 60% maschi, 40% femmine; età media 55 anni]. Si noti una potenziale mancanza di diversità in [Es. etnie, fasce d'età].

---

## 4. Dati di Valutazione

- **Dataset di Valutazione:** [Nome del dataset di test, es. porzione di test del dataset DRIVE].
- **Metriche di Performance:**
  - **Dice Score:** [Valore, es. 0.95]
  - **Intersection over Union (IoU):** [Valore, es. 0.91]
  - **Accuracy:** [Valore, es. 98.5%]
  - **ECC...**
- **Analisi per Sottogruppi:**
  - Le performance sono state valutate su sottogruppi demografici. Si è notato un leggero calo di performance (Dice -2%) su [Es. immagini di pazienti con diabete in stadio avanzato].

---

## 5. Considerazioni Etiche e Limitazioni

- **Bias Potenziali:** Il modello potrebbe avere performance inferiori su popolazioni sottorappresentate nel dataset di training. La qualità dell'immagine (illuminazione, artefatti) influenza significativamente l'output.
- **Robustezza:** Il modello è sensibile a variazioni di dominio (es. immagini da scanner diversi).
- **Raccomandazioni per l'Uso:** Usare come strumento di ausilio e validare sempre i risultati con un esperto del dominio.

---

## 6. Informazioni Aggiuntive

- **Risorse Computazionali:** Allenato su una GPU [Tipo di GPU, es. NVIDIA RTX 3090] per [Numero] ore.
- **Framework:** PyTorch
- **Commit Git del Codice di Training:** `[hash del commit]`
- **Versione DVC del Modello:** `[hash del modello in DVC]`