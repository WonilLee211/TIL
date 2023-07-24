CC = gcc
H = ../headerfile
TARGET = app.out
OBJS = test.o str.o

CFLAGS = -Wall
LDFLAGS = -lc

all : $(TARGET)
    
$(TARGET) : $(OBJS)
	$(CC) $(LDFLAGS) -o $@ $^ -I $(H)
    
.c.o :
	$(CC) $(CFLAGS) -c -o $@ $< -I $(H)
    
clean : 
	rm -f $(OBJS) $@