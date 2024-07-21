# class_static_methods_demo.py  

class Calculator:  
    calculation_type = "Arithmetic Operations"  

    @staticmethod  
    def add(a, b):  
        return a + b  

    @classmethod  
    def multiply(cls, a, b):  
        print(f"Performing {cls.calculation_type}...")  
        return a * b  

# Example usage:  
print(Calculator.add(2, 3))  # Output: 5  
print(Calculator.multiply(4, 5))  # Output: Performing Arithmetic Operations... 20