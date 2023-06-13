#include <sstream>
// from BSK
#include "architecture/utilities/avsEigenMRP.h"


static std::string toString(const Eigen::MatrixXd& mat){
    std::stringstream ss;
    ss << mat;
    return ss.str();
}

static void test(uint64_t simTimeNanos, Eigen::Vector3d r_I)
{

    printf("%llu", 285212672);

    // for signed ints
    printf("GravBodyData::computeGravityInertial: simTimeNanos %d\n", simTimeNanos);
    // for uint8_t, unint16_t
    // https://stackoverflow.com/a/50882761/4292910
    printf("incomingCmdMode: %hu\n", incomingCmdMode);
    // // for unint16_t (FFS cpp...)
    // printf("incomingFiringDuration: %hu\n", incomingFiringDuration);
    // for float
    printf("GravBodyData::computeGravityInertial: ri [%.15f, %.15f, %.15f]\n", r_I[0], r_I[1], r_I[2]);
}