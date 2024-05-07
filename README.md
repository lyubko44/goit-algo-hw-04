# goit-algo-hw-04

Результати:
* Time execution of Timsort for integers array: 0.023859209148213267
* Time execution of insertion sort for integers array: 0.6012200000695884
* Time execution of merge sort for integers array: 8.945729791885242

* Time execution of Timsort for strings array: 0.08727333298884332
* Time execution of insertion sort for strings array: 0.7425797081086785
* Time execution of merge sort for strings array: 9.787686750059947

* Time execution of Timsort for partially sorted array: 0.024337375070899725
* Time execution of insertion sort for partially sorted: 0.6363011251669377
* Time execution of merge sort for partially sorted: 9.053692458895966

Висоновок:
За наведеними даними видно, що алгоритм сортування Timsort працює найшвидше у всіх трьох випадках: для масивів цілих чисел, рядків і частково відсортованих масивів. Його час виконання набагато менше, ніж час виконання інших двох алгоритмів.

Далі, алгоритм сортування вставкою працює швидше за алгоритм сортування злиттям, але повільніше, ніж Timsort у всіх трьох випадках. Це може бути пов'язано з тим, що вставка працює ефективніше на вже впорядкованих або частково впорядкованих даних, ніж злиття.

Алгоритм сортування злиттям демонструє найпогіршу продуктивність у всіх трьох випадках. Це може бути пов'язано з його складністю, особливо на великих масивах даних.

У цілому, Timsort виявився найефективнішим алгоритмом сортування у цих експериментах, видаючи кращі часові результати для всіх типів вхідних даних.