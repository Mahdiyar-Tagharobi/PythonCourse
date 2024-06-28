t = int(input("Enter your time(second)"))

m_and_s = t % 3600

s = m_and_s % 60

print(f"converted time is {t // 3600}:{m_and_s // 60}:{s}")