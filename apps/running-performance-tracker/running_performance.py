# ============================================================
# RUNNING PERFORMANCE TRACKER
# ============================================================


# ============================================================
# 1. VARIABLES / INPUT
# ============================================================

name = input("Enter your name: ")
# input() — ввод строки

age = int(input("Enter your age: "))
# int() — преобразование в целое число

country = input("Enter your country: ")


# ============================================================
# 2. DISTANCE 1
# Дистанция 1 вводится ОДИН РАЗ
# ============================================================

distance_1 = float(input("Enter Distance 1 (km): "))


# -------------------------
# 2024
# -------------------------

time_1_2024 = input("Enter Time 1 for 2024 (h:m:s): ")
city_1_2024 = input("Enter City 1 for 2024: ")

hours_1_2024, minutes_1_2024, seconds_1_2024 = map(
    int,
    time_1_2024.split(":")
)

total_seconds_1_2024 = (
    hours_1_2024 * 3600
    + minutes_1_2024 * 60
    + seconds_1_2024
)

pace_1_2024 = total_seconds_1_2024 / distance_1 / 60


# -------------------------
# 2025
# -------------------------

time_1_2025 = input("Enter Time 1 for 2025 (h:m:s): ")
city_1_2025 = input("Enter City 1 for 2025: ")

hours_1_2025, minutes_1_2025, seconds_1_2025 = map(
    int,
    time_1_2025.split(":")
)

total_seconds_1_2025 = (
    hours_1_2025 * 3600
    + minutes_1_2025 * 60
    + seconds_1_2025
)

pace_1_2025 = total_seconds_1_2025 / distance_1 / 60


# -------------------------
# 2026
# -------------------------

time_1_2026 = input("Enter Time 1 for 2026 (h:m:s): ")
city_1_2026 = input("Enter City 1 for 2026: ")

hours_1_2026, minutes_1_2026, seconds_1_2026 = map(
    int,
    time_1_2026.split(":")
)

total_seconds_1_2026 = (
    hours_1_2026 * 3600
    + minutes_1_2026 * 60
    + seconds_1_2026
)

pace_1_2026 = total_seconds_1_2026 / distance_1 / 60


# ============================================================
# 3. DISTANCE 2
# Дистанция 2 тоже вводится ОДИН РАЗ
# ============================================================

distance_2 = float(input("Enter Distance 2 (km): "))


# -------------------------
# 2024
# -------------------------

time_2_2024 = input("Enter Time 2 for 2024 (h:m:s): ")
city_2_2024 = input("Enter City 2 for 2024: ")

hours_2_2024, minutes_2_2024, seconds_2_2024 = map(
    int,
    time_2_2024.split(":")
)

total_seconds_2_2024 = (
    hours_2_2024 * 3600
    + minutes_2_2024 * 60
    + seconds_2_2024
)

pace_2_2024 = total_seconds_2_2024 / distance_2 / 60


# -------------------------
# 2025
# -------------------------

time_2_2025 = input("Enter Time 2 for 2025 (h:m:s): ")
city_2_2025 = input("Enter City 2 for 2025: ")

hours_2_2025, minutes_2_2025, seconds_2_2025 = map(
    int,
    time_2_2025.split(":")
)

total_seconds_2_2025 = (
    hours_2_2025 * 3600
    + minutes_2_2025 * 60
    + seconds_2_2025
)

pace_2_2025 = total_seconds_2_2025 / distance_2 / 60


# -------------------------
# 2026
# -------------------------

time_2_2026 = input("Enter Time 2 for 2026 (h:m:s): ")
city_2_2026 = input("Enter City 2 for 2026: ")

hours_2_2026, minutes_2_2026, seconds_2_2026 = map(
    int,
    time_2_2026.split(":")
)

total_seconds_2_2026 = (
    hours_2_2026 * 3600
    + minutes_2_2026 * 60
    + seconds_2_2026
)

pace_2_2026 = total_seconds_2_2026 / distance_2 / 60


# ============================================================
# 4. LISTS
# Списки результатов
# ============================================================

results_1 = [
    [2024, distance_1, time_1_2024, city_1_2024, pace_1_2024],
    [2025, distance_1, time_1_2025, city_1_2025, pace_1_2025],
    [2026, distance_1, time_1_2026, city_1_2026, pace_1_2026]
]

results_2 = [
    [2024, distance_2, time_2_2024, city_2_2024, pace_2_2024],
    [2025, distance_2, time_2_2025, city_2_2025, pace_2_2025],
    [2026, distance_2, time_2_2026, city_2_2026, pace_2_2026]
]


# ============================================================
# 5. LEN()
# ============================================================

number_of_results_1 = len(results_1)
number_of_results_2 = len(results_2)


# ============================================================
# 6. AVERAGE PACE
# ============================================================

average_pace_1 = (
    pace_1_2024
    + pace_1_2025
    + pace_1_2026
) / 3

average_pace_2 = (
    pace_2_2024
    + pace_2_2025
    + pace_2_2026
) / 3


# ============================================================
# 7. BOOLEAN / COMPARISON
# ============================================================

is_long_run_1 = distance_1 >= 10
is_fast_1 = average_pace_1 <= 5

is_long_run_2 = distance_2 >= 10
is_fast_2 = average_pace_2 <= 5


# ============================================================
# 8. CONDITIONS
# ============================================================

if is_long_run_1 and is_fast_1:
    level_1 = "Advanced Runner"
elif is_long_run_1 or is_fast_1:
    level_1 = "Intermediate Runner"
else:
    level_1 = "Beginner Runner"


if is_long_run_2 and is_fast_2:
    level_2 = "Advanced Runner"
elif is_long_run_2 or is_fast_2:
    level_2 = "Intermediate Runner"
else:
    level_2 = "Beginner Runner"


# ============================================================
# 9. OUTPUT
# ============================================================

print()
print("=" * 75)
print(f"RUNNING PERFORMANCE — {name}")
print(f"Age: {age}")
print(f"Country: {country}")
print("=" * 75)


# ============================================================
# 10. TABLE — DISTANCE 1
# ============================================================

print()
print(f"DISTANCE 1 RESULTS — {distance_1} km")
print()

print(
    f"| {'Year':^6} | {'Distance':^10} | "
    f"{'Time':^10} | {'City':^15} | {'Pace':^10} |"
)

print(
    "|--------|------------|------------|-----------------|------------|"
)

print(
    f"| {2024:^6} | {distance_1:^10.1f} | "
    f"{time_1_2024:^10} | {city_1_2024:^15} | "
    f"{pace_1_2024:^10.2f} |"
)

print(
    f"| {2025:^6} | {distance_1:^10.1f} | "
    f"{time_1_2025:^10} | {city_1_2025:^15} | "
    f"{pace_1_2025:^10.2f} |"
)

print(
    f"| {2026:^6} | {distance_1:^10.1f} | "
    f"{time_1_2026:^10} | {city_1_2026:^15} | "
    f"{pace_1_2026:^10.2f} |"
)

print(
    "|--------|------------|------------|-----------------|------------|"
)

print(
    f"| {'AVG':^6} | {'':^10} | {'':^10} | {'':^15} | "
    f"{average_pace_1:^10.2f} |"
)


# ============================================================
# 11. TABLE — DISTANCE 2
# ============================================================

print()
print(f"DISTANCE 2 RESULTS — {distance_2} km")
print()

print(
    f"| {'Year':^6} | {'Distance':^10} | "
    f"{'Time':^10} | {'City':^15} | {'Pace':^10} |"
)

print(
    "|--------|------------|------------|-----------------|------------|"
)

print(
    f"| {2024:^6} | {distance_2:^10.1f} | "
    f"{time_2_2024:^10} | {city_2_2024:^15} | "
    f"{pace_2_2024:^10.2f} |"
)

print(
    f"| {2025:^6} | {distance_2:^10.1f} | "
    f"{time_2_2025:^10} | {city_2_2025:^15} | "
    f"{pace_2_2025:^10.2f} |"
)

print(
    f"| {2026:^6} | {distance_2:^10.1f} | "
    f"{time_2_2026:^10} | {city_2_2026:^15} | "
    f"{pace_2_2026:^10.2f} |"
)

print(
    "|--------|------------|------------|-----------------|------------|"
)

print(
    f"| {'AVG':^6} | {'':^10} | {'':^10} | {'':^15} | "
    f"{average_pace_2:^10.2f} |"
)


# ============================================================
# 12. FINAL INFORMATION
# ============================================================

print()
print("=" * 75)
print(f"Distance 1 average pace: {average_pace_1:.2f} min/km")
print(f"Distance 1 level: {level_1}")

print()

print(f"Distance 2 average pace: {average_pace_2:.2f} min/km")
print(f"Distance 2 level: {level_2}")

print()

print(f"Results for Distance 1: {number_of_results_1}")
print(f"Results for Distance 2: {number_of_results_2}")

print("=" * 75)
