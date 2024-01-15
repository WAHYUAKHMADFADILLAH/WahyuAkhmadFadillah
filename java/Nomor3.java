import java.util.ArrayList;
import java.util.Random;

public class Nomor3 {

    public static void main(String[] args) {
        ArrayList<PensilWarna> pensilBiru = new ArrayList<>();
        ArrayList<PensilWarna> pensilMerah = new ArrayList<>();
        ArrayList<PensilWarna> pensilHijau = new ArrayList<>();
        ArrayList<PensilWarna> pensilOranye = new ArrayList<>();
        ArrayList<PensilWarna> pensilHitam = new ArrayList<>();
        ArrayList<PensilWarna> pensilUngu = new ArrayList<>();

        Random random = new Random();
        int jumlahPensil = 20000;

        for (int i = 0; i < jumlahPensil; i++) {
            int warna = random.nextInt(6) + 1;
            PensilWarna pensil = new PensilWarna(warna);

            switch (warna) {
                case 1:
                    pensilBiru.add(pensil);
                    break;
                case 2:
                    pensilMerah.add(pensil);
                    break;
                case 3:
                    pensilHijau.add(pensil);
                    break;
                case 4:
                    pensilOranye.add(pensil);
                    break;
                case 5:
                    pensilHitam.add(pensil);
                    break;
                case 6:
                    pensilUngu.add(pensil);
                    break;
            }
        }

        System.out.println("Jumlah total pensil setiap warna:");
        System.out.println("Biru: " + pensilBiru.size());
        System.out.println("Merah: " + pensilMerah.size());
        System.out.println("Hijau: " + pensilHijau.size());
        System.out.println("Oranye: " + pensilOranye.size());
        System.out.println("Hitam: " + pensilHitam.size());
        System.out.println("Ungu: " + pensilUngu.size());

        System.out.println("\nProduksi pensil maksimum: " + max(pensilBiru, pensilMerah, pensilHijau, pensilOranye, pensilHitam, pensilUngu));
        System.out.println("Produksi pensil minimum: " + min(pensilBiru, pensilMerah, pensilHijau, pensilOranye, pensilHitam, pensilUngu));
    }

    private static int max(ArrayList<PensilWarna>... arrays) {
        int max = Integer.MIN_VALUE;
        for (ArrayList<PensilWarna> array : arrays) {
            max = Math.max(max, array.size());
        }
        return max;
    }

    private static int min(ArrayList<PensilWarna>... arrays) {
        int min = Integer.MAX_VALUE;
        for (ArrayList<PensilWarna> array : arrays) {
            min = Math.min(min, array.size());
        }
        return min;
    }
}

class PensilWarna {
    private int warna;

    public PensilWarna(int warna) {
        this.warna = warna;
    }

    public int getWarna() {
        return warna;
    }
}