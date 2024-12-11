class FinanceCalculator:
    def __init__(self, income):
        """
        Konstruktor untuk menyimpan pendapatan bulanan
        :param income: Pendapatan bulanan
        """
        self.income = income  # Menyimpan pendapatan bulanan

    def calculate_expenses(self, expenses):
        """
        Menghitung total pengeluaran bulanan dan sisa uang setelah pengeluaran.
        :param expenses: List yang berisi jumlah pengeluaran per kategori.
        :return: total pengeluaran dan sisa uang setelah pengeluaran.
        """
        total_expenses = sum(expenses)  # Menghitung total pengeluaran
        remaining_balance = self.income - total_expenses  # Sisa uang setelah pengeluaran
        return total_expenses, remaining_balance

    def calculate_savings(self, expenses, savings_percentage):
        """
        Menghitung jumlah tabungan berdasarkan persentase tabungan dari pendapatan.
        :param expenses: List pengeluaran bulanan
        :param savings_percentage: Persentase tabungan bulanan
        :return: Jumlah tabungan dan sisa uang setelah tabungan.
        """
        # Hitung pengeluaran dan sisa uang setelah pengeluaran
        total_expenses, remaining_balance = self.calculate_expenses(expenses)
        
        # Menghitung jumlah tabungan berdasarkan persentase
        savings = self.income * (savings_percentage / 100)
        remaining_balance_after_savings = remaining_balance - savings
        return savings, remaining_balance_after_savings

    def calculate_investment(self, savings, investment_rate, months):
        """
        Menghitung hasil investasi berdasarkan tabungan, tingkat pengembalian investasi, dan durasi.
        :param savings: Tabungan bulanan
        :param investment_rate: Tingkat pengembalian investasi dalam persen per bulan
        :param months: Durasi investasi dalam bulan
        :return: Hasil investasi setelah beberapa bulan
        """
        # Menghitung hasil investasi setelah beberapa bulan
        return savings * (1 + investment_rate / 100) ** months


def main():
    # Input pendapatan bulanan
    income = float(input("Masukkan pendapatan bulanan Anda: "))
    
    # Input pengeluaran
    expenses = []
    num_expenses = int(input("Berapa banyak kategori pengeluaran bulanan? "))

    for i in range(num_expenses):
        expense = float(input(f"Masukkan jumlah pengeluaran untuk kategori {i+1}: "))
        expenses.append(expense)

    # Input persentase tabungan
    savings_percentage = float(input("Masukkan persentase tabungan bulanan Anda: "))
    
    # Input informasi investasi
    investment_rate = float(input("Masukkan tingkat pengembalian investasi (dalam persen): "))
    months = int(input("Berapa bulan investasi Anda? "))

    # Membuat objek FinanceCalculator
    finance_calculator = FinanceCalculator(income)

    # Menghitung pengeluaran bulanan dan sisa uang setelah pengeluaran
    total_expenses, remaining_balance = finance_calculator.calculate_expenses(expenses)
    print(f"\nTotal pengeluaran bulanan: {total_expenses}")
    print(f"Sisa uang setelah pengeluaran: {remaining_balance}")

    # Menghitung tabungan bulanan dan sisa uang setelah tabungan
    savings, remaining_balance_after_savings = finance_calculator.calculate_savings(expenses, savings_percentage)
    print(f"Jumlah tabungan bulanan: {savings}")
    print(f"Sisa uang setelah tabungan: {remaining_balance_after_savings}")

    # Menghitung hasil investasi
    final_investment = finance_calculator.calculate_investment(savings, investment_rate, months)
    print(f"Hasil investasi setelah {months} bulan: {final_investment:.2f}")


if __name__ == "__main__":
    main()
