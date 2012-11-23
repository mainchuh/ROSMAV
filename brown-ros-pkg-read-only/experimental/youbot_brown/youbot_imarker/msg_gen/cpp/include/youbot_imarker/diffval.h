/* Auto-generated by genmsg_cpp for file /home/aarumbak/dev/brown/brown-ros-pkg/experimental/youbot_brown/youbot_imarker/msg/diffval.msg */
#ifndef YOUBOT_IMARKER_MESSAGE_DIFFVAL_H
#define YOUBOT_IMARKER_MESSAGE_DIFFVAL_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "std_msgs/Header.h"

namespace youbot_imarker
{
template <class ContainerAllocator>
struct diffval_ {
  typedef diffval_<ContainerAllocator> Type;

  diffval_()
  : header()
  , xx(0.0)
  , yy(0.0)
  , zz(0.0)
  {
  }

  diffval_(const ContainerAllocator& _alloc)
  : header(_alloc)
  , xx(0.0)
  , yy(0.0)
  , zz(0.0)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
   ::std_msgs::Header_<ContainerAllocator>  header;

  typedef float _xx_type;
  float xx;

  typedef float _yy_type;
  float yy;

  typedef float _zz_type;
  float zz;


private:
  static const char* __s_getDataType_() { return "youbot_imarker/diffval"; }
public:
  ROS_DEPRECATED static const std::string __s_getDataType() { return __s_getDataType_(); }

  ROS_DEPRECATED const std::string __getDataType() const { return __s_getDataType_(); }

private:
  static const char* __s_getMD5Sum_() { return "78a5bd8901d78d315b27b8ce4f334934"; }
public:
  ROS_DEPRECATED static const std::string __s_getMD5Sum() { return __s_getMD5Sum_(); }

  ROS_DEPRECATED const std::string __getMD5Sum() const { return __s_getMD5Sum_(); }

private:
  static const char* __s_getMessageDefinition_() { return "Header header\n\
\n\
float32 xx\n\
float32 yy\n\
float32 zz\n\
\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.secs: seconds (stamp_secs) since epoch\n\
# * stamp.nsecs: nanoseconds since stamp_secs\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
"; }
public:
  ROS_DEPRECATED static const std::string __s_getMessageDefinition() { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED const std::string __getMessageDefinition() const { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED virtual uint8_t *serialize(uint8_t *write_ptr, uint32_t seq) const
  {
    ros::serialization::OStream stream(write_ptr, 1000000000);
    ros::serialization::serialize(stream, header);
    ros::serialization::serialize(stream, xx);
    ros::serialization::serialize(stream, yy);
    ros::serialization::serialize(stream, zz);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint8_t *deserialize(uint8_t *read_ptr)
  {
    ros::serialization::IStream stream(read_ptr, 1000000000);
    ros::serialization::deserialize(stream, header);
    ros::serialization::deserialize(stream, xx);
    ros::serialization::deserialize(stream, yy);
    ros::serialization::deserialize(stream, zz);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint32_t serializationLength() const
  {
    uint32_t size = 0;
    size += ros::serialization::serializationLength(header);
    size += ros::serialization::serializationLength(xx);
    size += ros::serialization::serializationLength(yy);
    size += ros::serialization::serializationLength(zz);
    return size;
  }

  typedef boost::shared_ptr< ::youbot_imarker::diffval_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::youbot_imarker::diffval_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct diffval
typedef  ::youbot_imarker::diffval_<std::allocator<void> > diffval;

typedef boost::shared_ptr< ::youbot_imarker::diffval> diffvalPtr;
typedef boost::shared_ptr< ::youbot_imarker::diffval const> diffvalConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::youbot_imarker::diffval_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::youbot_imarker::diffval_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace youbot_imarker

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::youbot_imarker::diffval_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::youbot_imarker::diffval_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::youbot_imarker::diffval_<ContainerAllocator> > {
  static const char* value() 
  {
    return "78a5bd8901d78d315b27b8ce4f334934";
  }

  static const char* value(const  ::youbot_imarker::diffval_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x78a5bd8901d78d31ULL;
  static const uint64_t static_value2 = 0x5b27b8ce4f334934ULL;
};

template<class ContainerAllocator>
struct DataType< ::youbot_imarker::diffval_<ContainerAllocator> > {
  static const char* value() 
  {
    return "youbot_imarker/diffval";
  }

  static const char* value(const  ::youbot_imarker::diffval_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::youbot_imarker::diffval_<ContainerAllocator> > {
  static const char* value() 
  {
    return "Header header\n\
\n\
float32 xx\n\
float32 yy\n\
float32 zz\n\
\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.secs: seconds (stamp_secs) since epoch\n\
# * stamp.nsecs: nanoseconds since stamp_secs\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
";
  }

  static const char* value(const  ::youbot_imarker::diffval_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct HasHeader< ::youbot_imarker::diffval_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct HasHeader< const ::youbot_imarker::diffval_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::youbot_imarker::diffval_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.header);
    stream.next(m.xx);
    stream.next(m.yy);
    stream.next(m.zz);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct diffval_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::youbot_imarker::diffval_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::youbot_imarker::diffval_<ContainerAllocator> & v) 
  {
    s << indent << "header: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "xx: ";
    Printer<float>::stream(s, indent + "  ", v.xx);
    s << indent << "yy: ";
    Printer<float>::stream(s, indent + "  ", v.yy);
    s << indent << "zz: ";
    Printer<float>::stream(s, indent + "  ", v.zz);
  }
};


} // namespace message_operations
} // namespace ros

#endif // YOUBOT_IMARKER_MESSAGE_DIFFVAL_H

