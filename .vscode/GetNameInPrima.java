import java.util.ArrayList;

public class GetNameInPrima {

    public static void main(String[] args) {
        System.out.println("=========================");
        String nama ="Nama  : Wahyu Akhmad Fadillah";
        String kelas = "Kelas : 1C";
        int nim = 23090118;
        System.out.println(nama);
        System.out.println(kelas);
        System.out.println("nim   :"+nim);
        System.out.println("=========================");
        ArrayList<String> kendaraanList = new ArrayList<>();
        kendaraanList.add("Toyota");
        kendaraanList.add("Honda");
        kendaraanList.add("Suzuki");
        kendaraanList.add("BMW");

        boolean[] conditions = test(kendaraanList);

        for (boolean condition : conditions) {
            System.out.println("Karakternya == yang ada di array list :"+condition);
        }
    }

    public static boolean[] test(ArrayList<String> p) {
        int[] arrayPrima = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};

        boolean[] conditions = new boolean[p.size()];

        for (int i = 0; i < p.size(); i++) {
            String kendaraanMerk = p.get(i);

            int jumlahKarakter = kendaraanMerk.length();

            for (int prima : arrayPrima) {
                if (jumlahKarakter == prima) {
                    conditions[i] = true;
                    break;
                } else {
                    conditions[i] = false;
                }
            }
        }

        return conditions;
    }
}
