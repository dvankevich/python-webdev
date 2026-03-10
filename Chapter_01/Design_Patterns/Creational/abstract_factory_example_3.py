from abc import ABC, abstractmethod

# --- ДАНІ ---
RAW_DATA = {"period": "Травень 2024", "revenue": 150000, "expenses": 80000}

# --- ПРОДУКТИ: Звіти з логікою форматування ---

class Report(ABC):
    @abstractmethod
    def send(self, recipient: str):
        pass

class EmailHtmlReport(Report):
    def __init__(self, data):
        # Тут ми реально "готуємо" HTML-код
        self.content = f"<h1>Звіт за {data['period']}</h1><p>Прибуток: <b>{data['revenue']} грн</b></p>"

    def send(self, recipient: str):
        print(f"📧 Відправка Email на {recipient}...")
        print(f"Зміст: {self.content}\n[Система: Лист успішно надіслано через SMTP]")

class SlackJsonReport(Report):
    def __init__(self, data):
        # Slack любить JSON або розмітку blocks
        self.payload = {
            "text": f"🚀 *Новий звіт: {data['period']}*",
            "attachments": [{"fields": [{"title": "Дохід", "value": f"{data['revenue']}"}]}]
        }

    def send(self, channel_id: str):
        print(f"💬 Публікація в Slack-канал {channel_id}...")
        print(f"Payload: {self.payload}\n[Система: API запит 200 OK]")

# --- АБСТРАКТНА ФАБРИКА ---

class ReportingService(ABC):
    @abstractmethod
    def create_report(self, data) -> Report:
        pass

# --- КОНКРЕТНІ СЕРВІСИ (Фабрики) ---

class EmailService(ReportingService):
    def create_report(self, data):
        return EmailHtmlReport(data)

class SlackService(ReportingService):
    def create_report(self, data):
        return SlackJsonReport(data)
      

def monthly_closing_process(service: ReportingService, target: str):
    """
    Ця функція — ядро вашого бізнесу. 
    Вона проводить розрахунки та відправляє результат.
    Вона ВЗАГАЛІ не знає про Email чи Slack.
    """
    print("⚙️ Обробка фінансових даних...")
    # Уявімо, що тут складні розрахунки
    data = RAW_DATA 
    
    # Фабрика створює потрібний тип звіту
    report = service.create_report(data)
    
    # Надсилаємо (адресату або в канал)
    report.send(target)

# --- ВИКОРИСТАННЯ ---

# Сценарій А: Клієнт хоче звіт на пошту
monthly_closing_process(EmailService(), "manager@company.com")

print("-" * 30)

# Сценарій Б: Команда хоче сповіщення в Slack
monthly_closing_process(SlackService(), "#finance-alerts")