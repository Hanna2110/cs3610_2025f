from FurnitureAbstractfactory.FurnitureFactoryClass import FurnitureFactory

def getHannaFurniture():
    print("!!!!")
    hannaFurniture=[]
    hannaWishes=['smallchair','BigTable','MediumTable']
    
    for dream in hannaWishes:
        res=FurnitureFactory.get_furniture(dream)
        if res!=None:
            hannaFurniture.append(res)
            
    print(f"Hanna has {len(hannaFurniture)} items")
            
    for furniture in hannaFurniture:
        print(f"Hanna's furniture includes the {furniture.__class__} with {furniture.get_dimensions()}")
