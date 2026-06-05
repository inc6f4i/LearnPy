#042-1
male = ['슈퍼맨','심봉사','로미오','이몽룡','마루치']
female = ['원더우먼', '뺑덕어멈', '줄리엣', '성춘향', '아라치','a']
couples = zip(male, female, strict=True)
for couple in couples:
    print(couple)