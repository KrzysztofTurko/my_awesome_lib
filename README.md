📚 My Awesome Lib

My Awesome Lib to biblioteka Pythona, która dostarcza narzędzia do przetwarzania danych, obliczeń matematycznych oraz manipulacji tekstem. Jest przeznaczona dla programistów, którzy potrzebują prostych i efektywnych rozwiązań do codziennych zadań programistycznych.

🚀 Główne możliwości

📊 Przetwarzanie danych: Konwersja listy ciągów znaków na listę liczb całkowitych.

🧮 Obliczenia matematyczne: Proste operacje arytmetyczne, takie jak dodawanie.

📝 Manipulacja tekstem: Odwracanie ciągów znaków.

📦 Instalacja

Instalacja ręczna

Sklonuj repozytorium:

git clone https://github.com/KrzysztofTurko/my_awesome_lib.git

Przejdź do folderu projektu:

cd my_awesome_lib

Zainstaluj bibliotekę w trybie edytowalnym (jeśli dostępny jest setup.py):

pip install -e .

🛠️ Przykłady użycia

📊 Przetwarzanie danych

from my_awesome_lib.data_utils import convert_to_int

data = ["1", "2", "3"]
result = convert_to_int(data)
print(result)  # Output: [1, 2, 3]

🧮 Obliczenia matematyczne

from my_awesome_lib.math_tools import add_numbers

result = add_numbers(5, 3)
print(result)  # Output: 8

📝 Manipulacja tekstem

from my_awesome_lib.text_processing import reverse_string

result = reverse_string("hello")
print(result)  # Output: "olleh"

📜 Licencja

Ten projekt jest dostępny na licencji MIT. Szczegóły można znaleźć w pliku LICENSE.

👨‍💻 Autor

Autor: Krzysztof Turko

Email: krzysztof.turko1990@gmail.com

GitHub: https://github.com/KrzysztofTurko

🏷️ Wersja

Aktualna wersja: 1.0.0

