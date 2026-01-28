if __name__ == "__main__":
    symbols = 'ABC'
    
    symbol_generator = (symbol for symbol in symbols)
    
    for symbol in symbol_generator:
        print(symbol)
        
        