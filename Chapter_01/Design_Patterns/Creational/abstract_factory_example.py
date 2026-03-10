from abc import ABC, abstractmethod


class AbstractReport(ABC):

    @abstractmethod
    def create_month_report(self):
        pass

    @abstractmethod
    def create_quarter_report(self):
        pass

    @abstractmethod
    def create_year_report(self):
        pass


class PdfMonthReport:
    pass


class PdfQuarterReport:
    pass


class PdfYearReport:
    pass


class PdfReport(AbstractReport):

    def create_month_report(self):
        return PdfMonthReport()

    def create_quarter_report(self):
        return PdfQuarterReport()

    def create_year_report(self):
        return PdfYearReport()


class HtmlMonthReport:
    pass


class HtmlQuarterReport:
    pass


class HtmlYearReport:
    pass


class HtmlReport(AbstractReport):

    def create_month_report(self):
        return HtmlMonthReport()

    def create_quarter_report(self):
        return HtmlQuarterReport()

    def create_year_report(self):
        return HtmlYearReport()


class CsvMonthReport:
    pass


class CsvQuarterReport:
    pass


class CsvYearReport:
    pass


class CsvReport(AbstractReport):

    def create_month_report(self):
        return CsvMonthReport()

    def create_quarter_report(self):
        return CsvQuarterReport()

    def create_year_report(self):
        return CsvYearReport()
      
def generate_all_financial_reports(factory: AbstractReport):
    """
    Ця функція не знає, з яким форматом вона працює.
    Вона просто знає, що у фабрики є потрібні методи.
    """
    print(f"--- Генеруємо звіти за допомогою {factory.__class__.__name__} ---")
    
    month = factory.create_month_report()
    quarter = factory.create_quarter_report()
    year = factory.create_year_report()
    
    print(f"Створено: {type(month).__name__}")
    print(f"Створено: {type(quarter).__name__}")
    print(f"Створено: {type(year).__name__}\n")

# --- Клієнтський код ---

# Вибираємо PDF формат
pdf_factory = PdfReport()
generate_all_financial_reports(pdf_factory)

# Вибираємо HTML формат
html_factory = HtmlReport()
generate_all_financial_reports(html_factory)

# Вибираємо CSV формат
csv_factory = CsvReport()
generate_all_financial_reports(csv_factory)