//
// Author: jun10000 (https://github.com/jun10000)
//

#include <TimerOne.h>

// Onkyo RI Signal's Pin <Original: 2>
#define PIN 2
// Onkyo RI Signal's Max BitLength (Header + Body + Footer) <Original: 40>
#define BUFFERLENGTH 40
// Onkyo RI Signal Header's BitLength <Original: 3>
#define BUFFERLENGTH_HEADER 3
// Onkyo RI Signal Footer's BitLength <Original: 3>
#define BUFFERLENGTH_FOOTER 3
// Loop Interval of Acquiring Onkyo RI Signals <Original: 1000μs>
#define LOOPINTERVAL_US 1000
// The value of Adjusting LOOPINTERVAL_US <Original: 0μs>
#define LOOPINTERVALOFFSET_US 5

const bool BUFFER_HEADER[] = {1, 1, 1};
const bool BUFFER_FOOTER[] = {0, 0, 0};

enum RIBufferStatus
{
  RIBufferStatus_Storing,
  RIBufferStatus_Complete,
  RIBufferStatus_Wrong,
};

struct RIBuffer
{
  private:
    bool _buf[BUFFERLENGTH];
    int _cursor = 0;

    bool checkHeader()
    {
      int end = (_cursor <= BUFFERLENGTH_HEADER) ? _cursor - 1 : BUFFERLENGTH_HEADER - 1;
      for (int i = 0; i <= end; i++)
      {
        if (_buf[i] != BUFFER_HEADER[i]) { return false; }
      }

      return true;
    }

    bool checkFooter()
    {
      int offset = _cursor - BUFFERLENGTH_FOOTER;
      for (int i = 0; i < BUFFERLENGTH_FOOTER; i++)
      {
        if (_buf[i + offset] != BUFFER_FOOTER[i]) { return false; }
      }

      return true;
    }

  public:
    void add(bool value) { _buf[_cursor] = value; _cursor++; }
    void clear() { _cursor = 0; }
    int getLength() { return _cursor; }

    RIBufferStatus getStatus()
    {
      if (_cursor <= BUFFERLENGTH_HEADER)
      {
        if (checkHeader() == true) { return RIBufferStatus_Storing; }
        else { return RIBufferStatus_Wrong; }
      } else if (_cursor <= BUFFERLENGTH_HEADER + BUFFERLENGTH_FOOTER) {
        return RIBufferStatus_Storing;
      } else if (_cursor <= BUFFERLENGTH - 1) {
        if (checkFooter() == true) { return RIBufferStatus_Complete; }
        else { return RIBufferStatus_Storing; }
      } else {
        if (checkFooter() == true) { return RIBufferStatus_Complete; }
        else { return RIBufferStatus_Wrong; }
      }
    }

    String dump()
    {
      String ret = "";
      for (int i = 0; i < _cursor; i++)
      {
        char b = _buf[i] ? '1' : '0';
        ret.concat(b);
      }

      return ret;
    }
};

void callback_TimeElapsed()
{
  static RIBuffer buf;
  buf.add(digitalRead(PIN));

  switch (buf.getStatus())
  {
    case RIBufferStatus_Storing:
      break;
    case RIBufferStatus_Complete:
      Serial.println(buf.dump());
      buf.clear();
      break;
    case RIBufferStatus_Wrong:
      buf.clear();
      break;
  }
}

void setup()
{
  Serial.begin(9600);
  pinMode(PIN, INPUT);
  Timer1.initialize(LOOPINTERVAL_US + LOOPINTERVALOFFSET_US);
  Timer1.attachInterrupt(callback_TimeElapsed);
}

void loop()
{
  
}
