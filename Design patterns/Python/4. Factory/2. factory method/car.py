class Car:
    def specs(self) -> str:
        raise NotImplementedError
    

class SUV(Car):
    def specs(self) -> str:
        return "SUV with Hybrid engine and Automatic transmission"

class Sedan(Car):
    def specs(self) -> str:
        return "Sedan with Petrol engine and Automatic transmission"

class Coupe(Car):
    def specs(self) -> str:
        return "Coupe with V8 engine and Manual transmission"