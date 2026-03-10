from abc import ABC, abstractmethod

# --- АБСТРАКТНІ ПРОДУКТИ (Інтерфейси для самих звітів) ---

class Report(ABC):
    @abstractmethod
    def save(self, filename: str):
        pass

# --- КОНКРЕТНІ ПРОДУКТИ (Реалізація логіки форматування) ---

class HtmlMonthReport(Report):
    def save(self, filename: str):
        print(f"📄 Зберігаємо HTML-звіт: {filename}.html")
        print("<html><body><h1>Місячний звіт</h1><table>...</table></body></html>")

class CsvMonthReport(Report):
    def save(self, filename: str):
        print(f"📊 Зберігаємо CSV-звіт: {filename}.csv")
        print("ID;Дата;Сума\n1;2024-05-01;500.00")

# (Аналогічно можна додати річні та квартальні класи)

# --- АБСТРАКТНА ФАБРИКА ---

class AbstractReportFactory(ABC):
    @abstractmethod
    def create_month_report(self) -> Report:
        pass

# --- КОНКРЕТНІ ФАБРИКИ ---

class HtmlReportFactory(AbstractReportFactory):
    def create_month_report(self):
        return HtmlMonthReport()

class CsvReportFactory(AbstractReportFactory):
    def create_month_report(self):
        return CsvMonthReport()
      
def business_logic(factory: AbstractReportFactory):
    """
    Ця функція — це ваш 'двигун'. 
    Вона не знає, БУДЕ ЦЕ HTML чи CSV. 
    Вона просто знає, що фабрика дасть їй звіт.
    """
    report = factory.create_month_report()
    # Логіка програми...
    report.save("financial_may_2024")

# --- Користувач вибирає формат ---
user_choice = input("Який формат бажаєте? (html/csv): ").lower()

if user_choice == "html":
    current_factory = HtmlReportFactory()
elif user_choice == "csv":
    current_factory = CsvReportFactory()
else:
    print("Невідомий формат!")
    exit()

# Запускаємо логіку з обраною фабрикою
business_logic(current_factory)