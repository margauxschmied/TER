public final class Stopwatch extends StopwatchAccessor {
    public static final int START_MODE=0;
    public static final int UNSTART_MODE=1;
    public Stopwatch(int mode){
        if (mode == START_MODE){start();}
    }
    public Stopwatch(){
        this(UNSTART_MODE);
    }
    public void start() {
        if (start != -1){
            throw new IllegalStateException("Problem: Stopwatch successive calls of function start()");
        }
        start = System.nanoTime();
    }
    public Stopwatch stop() {
        if (start == -1){
            throw new IllegalStateException("Problem: Stopwatch function stop() is called without a corresponding start() call");
        }
        last=(System.nanoTime() - start);
        cumul += last;
        start=-1;
        numCumuls++;
        return this;
    }
    public Stopwatch split(){
        if (start == -1) {
            throw new IllegalStateException("Problem: Stopwatch function split() is called without a corresponding start() call");
        }
        final long time=System.nanoTime();
        last=time -start;
        cumul += last;
        start=time;
        numCumuls++;
        return this;
    }
    public void reset(){
        start=-1;
        last=cumul=numCumuls=0;
    }
}