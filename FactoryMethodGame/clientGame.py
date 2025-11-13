from FactoryMethodGame.EnemyFactoryClass import EnemyFactory

def game():
    enemies=['ZOMBIE','RoboT','vampirE','VAMPIRE1']
    
    myEnemies=list(map(EnemyFactory.createEnemy,enemies))
    
    for myEnemy in myEnemies:
        if myEnemy:
            print(myEnemy.attack())