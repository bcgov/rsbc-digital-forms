import { useRecoilValue } from 'recoil';
import { userAtom } from '../../atoms/users';

export const InitialValues = () => {
    const user = useRecoilValue(userAtom);

    return {
        "IRP": false,
        "VI": false,
        "24Hour": false,
        "12Hour": false,
        "drivers-licence-jurisdiction": '',
        "drivers-number":'',
        "last-name":'',
        "given-name":'',
        "dob": '',
        "address":'',
        "city":'',
        "phone": '',
        "prov-state":'',
        "postal-code":'',
        "vehicle-jurisdiction": '',
        "plate-number": '',
        "registration-number": '',
        "vehicle-year": '',
        "vehicle-make-model": '',
        "vehicle-style": '',
        "vehicle-colour": [],
        "nsc-prov-state": '',
        "vin-number": '',
        "nsc-number": '',
        "owned-by-corp" : false,
        "corp-name": '',
        "owner-last-name":'',
        "owner-first-name": '',
        "registered-owner-address": '',
        "registered-owner-phone": '',
        "registered-owner-city": '',
        "registered-owner-prov-state": '',
        "registered-owner-postal": '',
        "officer-lastname":user.last_name || '',
        "officer-prime-id":user.badge_number || '',
        "officer-agency":user.agency || ''

    }
}