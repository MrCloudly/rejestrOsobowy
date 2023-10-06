import inspect
import Models

# klasa Controller nadzoruje Typy dostępne w Models, może je preparować dla metod dostępnych w ModelClass.
class Controller:

    @staticmethod
    def InitType(typ,**parameters):
        objectInit = None
        if typ == "*":
            createdObj = []
            avaiableTypes = Controller.get_types()
            for obj in avaiableTypes:
                ClassObj = getattr(Models, obj)
                objectInit = ClassObj(**parameters)
                createdObj.append(objectInit)
            return createdObj
        if typ in Controller.get_types():
            ClassObj = getattr(Models, typ)
            objectInit = ClassObj(**parameters)
            return objectInit
        return None

    #zwraca wszystkie typy dostępne w Models
    @staticmethod
    def get_types():
        classes = []
        for _, obj in inspect.getmembers(Models):
            if inspect.ismodule(obj):
                for _, class_obj in inspect.getmembers(obj):
                    if inspect.isclass(class_obj):
                        if(class_obj.__name__ != "ModelType"):
                            classes.append(class_obj.__name__)
        return classes